#!/usr/bin/env groovy

/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '58.0',
  platform: 'Windows 10'
]

pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        deleteDir()
        checkout scm
        stash 'workspace'
      }
    }
    stage('Lint') {
      steps {
        deleteDir()
        unstash 'workspace'
        ansiColor('xterm') {
          sh """
            pip install -r requirements/flake8.txt
            flake8
            """
        }
      }
    }
    stage('Accessibility') {
      steps {
        unstash 'workspace'
        ansiColor('xterm') {
          sh """
            npm install
            git init
            npm run package
            mkdir results
            tox -e a11y
            """
        }
      }
      post {
        always {
          stash includes: 'results/*', name: 'results'
          archiveArtifacts 'results/*'
        }
      }
    }
    stage('Test') {
      steps {
        unstash 'workspace'
        ansiColor('xterm') {
          sh """
            npm install
            git init
            npm run package
            mkdir results
            tox -e py3-integration-tests
            """
        }
      }
      post {
        always {
          stash includes: 'results/*', name: 'results'
          archiveArtifacts 'results/*'
        }
      }
    }
  }
}
