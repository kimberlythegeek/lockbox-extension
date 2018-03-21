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
            python -m flake8
            """
        }
      }
    }
    stage('Test') {
      environment {
        SAUCELABS = credentials('SAUCELABS')
      }
      steps {
        unstash 'workspace'
        ansiColor('xterm') {
          sh """
            npm install
            git init
            npm run package
            mkdir results
            tox -e sauce
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
