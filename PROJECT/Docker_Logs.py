import docker
import subprocess
'''
docker run mcr.microsoft.com/windows/servercore:ltsc2022
import docker
client = docker.from_env()

You can now run containers:

>>> client.containers.run("ubuntu", "echo hello world")
'hello world\n'

You can run containers in the background:

>>> client.containers.run("bfirsh/reticulate-splines", detach=True)
<Container '45e6d2de7c54'>

You can manage containers:

>>> client.containers.list()
[<Container '45e6d2de7c54'>, <Container 'db18e4f20eaa'>, ...]

>>> container = client.containers.get('45e6d2de7c54')

>>> container.attrs['Config']['Image']
"bfirsh/reticulate-splines"

>>> container.logs()
"Reticulating spline 1...\n"

>>> container.stop()
'''


def get_logs():
    client = docker.from_env()
    client.containers.run('mcr.microsoft.com/windows/servercore:ltsc2022')
    client.images.list()
    container=client.containers.get('')#containerin ismi yazılmalı nuarası yazılacak

    #docker kurulduktan sonra exe dosyasının bu dockera atılmalı ve çalıştırılmalı
    logs=container.logs()

    return logs


def docker():
    logs=subprocess.run('docker.sh')
    return logs