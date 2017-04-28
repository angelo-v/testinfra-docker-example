import pytest
import docker

@pytest.fixture(scope="module", autouse=True)
def container(client, image):
    container = client.containers.run(image.id, name="jenkins_test_container", detach=True)
    yield container
    container.remove(force=True)

def test_current_user_is_jenkins(User):
    assert User().name == "jenkins"
    assert User().group == "jenkins"

def test_jenkins_is_running(Process):
    jenkins = Process.get(comm="java")
    assert jenkins.args == "java -jar /usr/share/jenkins/jenkins.war"
    assert jenkins.user == "jenkins"

def test_maven_is_installed(Package):
    assert Package("maven").is_installed
