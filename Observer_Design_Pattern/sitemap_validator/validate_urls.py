import requests
import xml.etree.ElementTree as ET
from collections import Counter

class RequestSender:
    def send_request(self, url):
        """
        Send a GET request to the specified URL and return True if the response status is OK, otherwise return False.    
        Args:
            url (str): The URL to send the request to.
        Returns:
            bool: True if the response status is OK, False otherwise.
        """
        try:
            response = requests.get(url)
            return response.ok
        except requests.RequestException:
            return False

class SitemapParser:
    def __init__(self, xml_content):
        """
        Initialize the class with the provided XML content.
        Args:
            xml_content (str): The XML content to be stored.
        """
        self.xml_content = xml_content

    def extract_urls(self):
        """
        Extracts unique URLs from the XML content and identifies duplicate URLs.
        
        Returns:
            urls: list of unique URLs
            duplicate_urls: list of duplicate URLs
        """
        urls = []
        duplicate_urls = []
        try:
            root = ET.fromstring(self.xml_content)
            for url_element in root.findall('.//url/loc'):
                url = url_element.text.strip()
                if url in urls:
                    duplicate_urls.append(url)
                else:
                    urls.append(url)
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
        return urls, duplicate_urls

class LoggingObserver:
    def __init__(self, output_file):
        """
        Initialize the class with the given output file.
        Args:
            output_file (str): The path to the output file.
        """
        self.output_file = output_file

    def notify(self, url, success):
        """
        Appends a message to the output file if the access to the given URL failed.
        
        Args:
            url (str): The URL that was attempted to be accessed.
            success (bool): Indicates whether the access was successful or not.
        """
        with open(self.output_file, 'a') as f:
            if not success:
                f.write(f"Failed to access: {url}\n")

class SitemapRequester:
    def __init__(self, request_sender, observers=None, output_file="sitemap_validator_output.txt"):
        """
        Initialize the SitemapValidator with the request sender, observers, and output file.
        Args:
            request_sender (RequestSender): The object responsible for sending HTTP requests.
            observers (list, optional): List of observer objects to notify of validation events. Defaults to None.
            output_file (str, optional): The file to write validation output to. Defaults to "sitemap_validator_output.txt".
        """
        self.request_sender = request_sender
        self.observers = observers or []
        self.output_file = output_file

    def add_observer(self, observer):
        """
        Adds a new observer to the list of observers.
        Args:
            observer: The observer to be added.
        """
        self.observers.append(observer)

    def remove_observer(self, observer):
        """
        Removes the specified observer from the list of observers.
        Args:
            observer: The observer to be removed.
        """
        self.observers.remove(observer)

    def send_requests(self, sitemap_url):
        """
        Send requests to the URLs extracted from the sitemap and write the result to an output file.
        Args:
            sitemap_url (str): The path to the sitemap file.
        """
        success_count = 0
        failure_count = 0
        failure_urls = []
        duplicate_urls = []

        with open(sitemap_url, 'r') as f:
            xml_content = f.read()
            parser = SitemapParser(xml_content)
            urls, duplicate_urls = parser.extract_urls()

            for url in urls:
                success = self.request_sender.send_request(url)
                if success:
                    success_count += 1
                else:
                    failure_count += 1
                    failure_urls.append(url)
                self.notify_observers(url, success)

        with open(self.output_file, 'w') as f:
            f.write(f"Success count: {success_count}\n")
            f.write(f"Failure count: {failure_count}\n")
            f.write("Failure URLs:\n")
            for url in failure_urls:
                f.write(f"{url}\n")
            f.write("\nDuplicate URLs:\n")
            for url, count in Counter(duplicate_urls).items():
                f.write(f"{url} (Count: {count})\n")

    def notify_observers(self, url, success):
        """
        Notifies all observers with the given URL and success status.
        Args:
            url (str): The URL to be notified.
            success (bool): The success status to be notified.
        """
        for observer in self.observers:
            observer.notify(url, success)

if __name__ == "__main__":
    request_sender = RequestSender()
    logging_observer = LoggingObserver("sitemap_validator_output.txt")

    sitemap_requester = SitemapRequester(request_sender)
    sitemap_requester.add_observer(logging_observer)

    sitemap_requester.send_requests("listing_sitemap_Feb10.xml")
    # sitemap_requester.send_requests("dealership_sitemap_feb.xml")
