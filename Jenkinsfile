import calpoly.filebeat.Filebeat
import calpoly.sonarqube.SonarQube

def fb = new Filebeat(env, steps)
def sq = new SonarQube(env, steps)

def type = 'selenium'
def ts = new Date().getTime()

def project = 'GroooooovyTest'

node {

    stage('Clone Repository') {
        git branch: BRANCH, credentialsId: env.GIT_KEY_ID, url: REPO
        sh "rm -rf testing_credentials"
        sh "git clone ${env.CREDENTIALS_REPO}"
    }

    stage('Run Synthetic Tests') {
        sh "rm -rf logs"
        sh "mkdir -p logs"
        sh "rm -rf .pyenv-Python3"


        withPythonEnv('Python3'){
            pysh "\$(pwd)/.pyenv-Python3/bin/pip install -r requirements.txt"
            pysh "\$(pwd)/.pyenv-Python3/bin/python3 runner.py --build_id ${env.BUILD_ID} --driver ${DRIVER} --headless yes --branch ${BRANCH} --config \$(pwd)/testing_credentials/polylearn_acceptance_tests.ini >> logs/${type}-${ts}_log.json"
        }
    }
    
    stage('Static Code Analysis') {
        String inclusions = ''
        String exclusions = 'sonar-scanner*'
        String testInclusions = ''
        String testExclusions = 'sonar-scanner*'

        sq.Scan(inclusions, exclusions, testInclusions, testExclusions, project)
    }

    stage('Ship Logs') {
        fb.LogPush(type)
    }
}
