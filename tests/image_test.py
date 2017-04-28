import pytest
import docker

@pytest.fixture(scope="module", autouse=True)
def container():
    client = docker.from_env()
    container = client.containers.run('jenkins', name="jenkins_test_container", detach=True)
    yield container
    container.remove(force=True)

def test_current_user_is_jenkins(User):
    assert User().name == "jenkins"
    assert User().group == "jenkins"

def test_jenkins_is_running(Process):
    assert Process.get(user="jenkins", comm="java").args == "java -jar /usr/share/jenkins/jenkins.war"
