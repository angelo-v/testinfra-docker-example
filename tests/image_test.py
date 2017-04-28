import pytest

def test_current_user_is_jenkins(User):
    assert User().name == "jenkins"
    assert User().group == "jenkins"

def test_jenkins_is_running(Process):
    assert Process.get(user="jenkins", comm="java").args == "java -jar /usr/share/jenkins/jenkins.war"
