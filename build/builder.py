#!/usr/bin/env python

import os
import sys
from package import *
from helper import *

def create(database):
   if not os.path.exists(repository_path):
      os.makedirs(repository_path)

   sys.path.append(packages_path)

   for directory in get_packages():
      __import__(directory + '.package')
      os.chdir(packages_path + '/' + directory)
      module = sys.modules[directory + '.package']
      package = Package(module, directory)

   os.chdir(repository_path)
   os.system('repo-add ./' + database + '.db.tar.gz ./*.pkg.tar.xz')

def deploy():
   for directory in get_packages():
      module = packages_path + '/' + directory
      if output('git status %s --porcelain | sed s/^...//' % module):
         print(
            'git add ' + module + ' && ' + \
            'git commit -m "Bot: Add ' + module + ' last update on ' + version(module) + ' version"')

   if is_travis():
      repository = git_repository()
      os.system('git push https://${GITHUB_TOKEN}@%s HEAD:master' % repository)

def main(argv):
   if len(argv) == 2 and argv[0] == 'create':
      create(argv[1])
   elif len(argv) == 1 and argv[0] == 'deploy':
      deploy()

if __name__ == '__main__':
   if os.getuid() == 0:
      print('This file needs to be not execute as root.')
      sys.exit(2)

   main(sys.argv[1:])