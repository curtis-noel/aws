'''
Created on Mar 26, 2018

@author: curtis
'''

import boto3
import random
import string
import logging

logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

if __name__ == '__main__':
    rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])
    s = rand_str(10) + "-temp"
    logging.info("Starting - bucket name: " + s)
    logging.info("opening session")
    session = boto3.Session(profile_name='default')
    logging.info("getting s3 resource")
    s3 = session.resource('s3')
    logging.info("creating bucket")
    s3.create_bucket(Bucket = s)
    logging.info("deleting bucket")
    bucket = s3.Bucket(s)
    bucket.delete();
    logging.info("finished")