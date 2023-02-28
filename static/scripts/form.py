import pyscript
import pyodide
import json
from pyodide.http import pyfetch
import js

async def make_request(url,method,body):
    csrf = js.document.getElementsByName('csrfmiddlewaretoken')[0].value

    headers = {
        'X-Requested-With' : 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'X-CSRFToken' : csrf
    }

    response = await pyfetch(
        url = url,
        method=method,
        body=body,
        headers=headers
    )
    return await response.json()

async def create_account(e):
    first_name = js.document.querySelector('#first_name')
    last_name = js.document.querySelector('#last_name')
    email = js.document.querySelector('#email')


    body = json.dumps({'first_name':first_name.value,'last_name':last_name.value,'email':email.value})

    response = await make_request(url='/',method='POST',body=body)

    if response.get('errors'):
        first_name.classList.add('is-invalid')
        last_name.classList.add('is-invalid')
        email.classList.add('is-invalid')
    else:
        first_name.classList= 'form-control is-valid'
        last_name.classList = 'form-control is-valid'
        email.classList = 'form-control is-valid'

        ul = js.document.getElementById('details')
        li = js.document.createElement('li')

        ul.appendChild(li)

        li.innerHTML = response['first_name'] + ' ' + response['last_name'] + ' ' + response['email']



def main():
    creat_account = js.document.getElementById('creat_account')
    creat_account.addEventListener('click',pyodide.create_proxy(create_account))

main()