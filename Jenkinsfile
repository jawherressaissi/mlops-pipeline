pipeline {

    agent any


    stages {
        stage ('GIT') {
            steps {
               echo "Getting Project from Git"; 
		sh "git checkout -b master"
                git branch: "master", 
                    url: "https://github.com/jawherressaissi/mlops-pipeline.git";
		}
        }
       
        stage("Build") {
            steps {
                sh "mvn clean package -DskipTests"
            }
        }

        stage("Unit tests") {
            steps {
                sh "mvn test -Dmaven.test.skip=false -Dspring.profiles.active=test"
            }
        }

        stage("SRC Analysis Testing") {
            steps {
                sh "mvn sonar:sonar"
            }
        }

        stage("Deploy Artifact to private registry") {
            steps {
                sh "mvn deploy"
            }
        }

        
        stage("Build Docker image") {
            steps {
                sh "docker build -t demo ."
            }
        }

        stage("Deploy Docker Image to private registry") {
            steps {
                sh "docker tag demo jawherrs/devops"
		sh "docker push jawherrs/demo"
            }
        }
        
    }
   
    post {
        always {
            cleanWs()
        }
    }
    
}