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
                //sh "docker build -t sa-model ."
                sh "docker stop sa-model && docker rm sa-model"
                sh "docker run -t -d --name sa-model sa-model"
                //sh "docker start sa-model"
            }
        }

        stage("Train") {
            steps {
                //sh "docker container exec sa-model python3 model.py"
                script {
                    // Define MLflow parameters
                    def mlflowContainerName = "mlflow-sa-container"  // Name of your MLflow Docker container
                    def experimentName = "MLOps SA Pipeline"  // Name of the MLflow experiment

                    // Start an MLflow run in the Docker container
                    sh "docker run -d --name ${mlflowContainerName} -p 5000:5000 ghcr.io/mlflow/mlflow server"
                    sh "mlflow experiments create -n ${experimentName} -u http://localhost:5000"

                    // Log the trained model and other artifacts to MLflow
                    sh "mlflow run . --experiment-name ${experimentName} -u http://localhost:5000"
                    sh "mlflow log_artifacts . --experiment-name ${experimentName} -u http://localhost:5000"

                    // Stop and remove the MLflow Docker container
                    sh "docker stop ${mlflowContainerName}"
                    sh "docker rm ${mlflowContainerName}"
                }
            }
        }

        stage("Test") {
            steps {
                sh "docker exec -d sa-model cat test_metadata.json "
                sh '''
                    val_acc=$(docker container exec sa-model jq .accuracy test_metadata.json)
                    threshold=0.8

                    if echo "$threshold > $val_acc" | bc -l | grep -q 1; then
                        echo 'Validation accuracy is lower than the threshold, process stopped'
                    else
                        echo 'Validation accuracy is higher than the threshold'
                    fi
                '''
                
            }
        }

        stage('MLflow Tracking') {
            steps {
                // Set up MLflow tracking
                script {
                    // Define MLflow parameters
                    def mlflowContainerName = "mlflow-sa-container"  // Name of your MLflow Docker container
                    def experimentName = "MLOps SA Pipeline"  // Name of the MLflow experiment

                    // Start an MLflow run in the Docker container
                    sh "docker run -d --name ${mlflowContainerName} -p 5000:5000 ghcr.io/mlflow/mlflow server"
                    sh "mlflow experiments create -n ${experimentName} -u http://localhost:5000"

                    // Log the trained model and other artifacts to MLflow
                    sh "mlflow run . --experiment-name ${experimentName} -u http://localhost:5000"
                    sh "mlflow log_artifacts . --experiment-name ${experimentName} -u http://localhost:5000"

                    // Stop and remove the MLflow Docker container
                    sh "docker stop ${mlflowContainerName}"
                    sh "docker rm ${mlflowContainerName}"
                }
            }
        }

        stage("Deploy") {
            steps {
                sh "docker container exec sa-model python3 -m flask run"
            }
        }
        
    }
   
    post {
        always {
            cleanWs()
        }
    }
    
}