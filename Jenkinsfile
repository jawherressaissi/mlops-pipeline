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
       
        stage("Train") {
            steps {
                sh "python3 model.py"
            }
        }

        stage("Test") {
            steps {
                sh '''
                    val_acc=$(sudo -S jq .accuracy /home/vagrant/mlops-pipeline/train_metadata.json)
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