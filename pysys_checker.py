# -*- coding: utf-8 -*-
import sys
import getopt

class Pysys(object):
    
    log_path = ''

    def usage(self):
        print 'PyTest.py usage:'
        print '-h,--help: print help message.'
        print '-v, --version: print script version'
        print '-o, --output: input an output verb'
    def version(self):
        print 'PyTest.py 1.0.0.0.1'
    def outPut(self, args):
        print 'Hello, %s'%args
    def main(self, argv):
        longopts = ['help=', 'version=', 'output=', 'log_path=']
        try:
            opts, args = getopt.getopt(argv[1:],'hh:l', longopts)
        except getopt.GetoptError, err:
            print str(err)
            self.usage()
            sys.exit(2)
        for o, a in opts:
            if o in ('-h', '--help'):
                self.usage()
                sys.exit(1)
            elif o in ('-v', '--version'):
                self.version()
                sys.exit(0)
            elif o in ('-o', '--output'):
                self.outPut(a)
                sys.exit(0)
            elif o in ('-l', '--log_path',):
                log_path = a
                return log_path
            else:
                print 'unhandled option'
                sys.exit(3)