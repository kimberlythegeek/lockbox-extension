#!/usr/bin/env groovy

pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        deleteDir()
        checkout scm
        ansiColor('xterm') {
          sh """
            npm install
            git init
            npm run package
            """
        }
        stash 'workspace'
      }
    }
    stage('Lint') {
      steps {
        deleteDir()
        unstash 'workspace'
        ansiColor('xterm') {
          sh "tox -e flake8"
        }
      }
    }
    stage('Accessibility') {
      steps {
        unstash 'workspace'
        ansiColor('xterm') {
          sh """
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
          sh "tox -e py3"
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
