#! /usr/bin/env python
# encoding: utf-8

import os

def configure( cnf ):

    if cnf.env.DEST_OS is 'linux':
        cnf.check_cxx( lib='pthread' )


def build( bld ):

    use_flags = []

    if bld.env.DEST_OS is 'linux':

        ext_paths = ['/usr/lib/i386-linux-gnu'
                   , '/usr/lib/arm-linux-gnueabi'
                   , '/usr/lib/x86_64-linux-gnu']

        bld.read_shlib( 'pthread'
                      , paths = ext_paths )
        use_flags += ['pthread']

    if bld.env.DEST_OS == 'android':
	    bld.env.DEFINES_GMOCK_SHARED += ['GTEST_OS_LINUX_ANDROID=1']

    use_flags += ['GMOCK_SHARED']

    bld.stlib( features = 'cxx'
	         , source   = ['src/gtest-all.cc']
	         , target   = 'gtest'
	         , includes = ['include'
                         , '.']
             , export_includes = ['include']
             , use      = use_flags )
