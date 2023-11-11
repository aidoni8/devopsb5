#Given a list of website URLs, write a Python program
# to create a new list that contains only those URLs which 
# belong to the domain 'example.com'. Assume the original list
# is of the format 
# ['https://example.com/page1', 'https://othersite.org/about',
#   'http://example.com/home', 'https://yetanothersite.net/blog'].


#Way you can understand if a url belongs to certain domain is
#simply by checking if url contains the domain name.


domain_name = "example.com"
list_of_urls = ['https://example.com/page1', 'https://othersite.org/about', 'http://example.com/home', 'https://yetanothersite.net/blog']
urls_with_domain = []
for url in list_of_urls:
    if domain_name in url:
        urls_with_domain.append(url)

print(urls_with_domain)







