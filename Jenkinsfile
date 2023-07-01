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
                sh "pwd"
            }
        }
        
    }
   
    post {
        always {
            cleanWs()
        }
    }
    
}