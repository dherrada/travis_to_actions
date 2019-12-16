import os
with open('bundle_libs.txt', 'r') as F:
    for line in F:
        os.chdir('/home/dherrada/travis_to_actions/repositories1/')
        os.system('git clone {}'.format(line))
