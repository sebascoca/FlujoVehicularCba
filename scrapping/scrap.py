import httpx


url = 'https://app.powerbi.com/view?r=eyJrIjoiMjUyMWVjNzctNDc4Ny00MzQyLWI0NjktNDYxNzU5ZDE1MDM5IiwidCI6ImU4YjUzOTJiLWM1NmQtNGM4Ni1iNjU4LWJjYmFhNzM1ZDFjZCIsImMiOjR9'

r = httpx.get(url)

print(r.status_code)
print(r.headers['content-type'])
print(r.text)
