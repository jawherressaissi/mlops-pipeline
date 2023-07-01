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
       
        stage("Build Docker image") {
            steps {
                sh "sudo -S docker build -t sa-model ."
                sh "sudo -S docker run -d --name sa-model sa-model"
            }
        }

        stage("Train") {
            steps {
                sh "sudo -S docker container exec sa-model python3 model.py"
            }
        }

        stage("Test") {
            steps {
                sh '''
                    sudo -S docker container exec sa-model cat /home/vagrant/test_metadata.json 
                    val_acc=$(sudo -S docker container exec sa-model jq .accuracy /home/vagrant/mlops-pipeline/train_metadata.json)
                    threshold=0.8

                    if echo "$threshold > $val_acc" | bc -l | grep -q 1; then
                        echo 'Validation accuracy is lower than the threshold, process stopped'
                    else
                        echo 'Validation accuracy is higher than the threshold'
                    fi
                '''
            }
        }
        
    }
   
    post {
        always {
            cleanWs()
        }
    }
    
}