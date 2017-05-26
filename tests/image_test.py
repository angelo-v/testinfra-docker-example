import pytest
import docker

testinfra_hosts = ["docker://jenkins_test_container"]

@pytest.fixture(scope="module", autouse=True)
def container(client, image):
    container = client.containers.run(image.id, name="jenkins_test_container", detach=True)
    yield container
    container.remove(force=True)

def test_current_user_is_jenkins(host):
    assert host.user().name == "jenkins"
    assert host.user().group == "jenkins"

def test_jenkins_is_running(host):
    jenkins = host.process.get(comm="java")
    assert jenkins.args == "java -jar /usr/share/jenkins/jenkins.war"
    assert jenkins.user == "jenkins"

def test_maven_is_installed(host):
    assert host.package("maven").is_installed
