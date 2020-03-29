import click
import os

from dotenv import load_dotenv
from webdav3.client import Client

dotenv_path = os.path.join(os.getcwd(), '.env')

if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)

client = Client({
    'webdav_hostname': os.getenv('PUTIO_HOSTNAME'),
    'webdav_login': os.getenv('PUTIO_LOGIN'),
    'webdav_password': os.getenv('PUTIO_PASSWORD'),
})

@click.command()
def list(path=''):
    click.echo("\n".join(client.list(path)))

def main():
    list()

if __name__ == '__main__':
    main()
