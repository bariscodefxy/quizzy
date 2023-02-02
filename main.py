#!/usr/bin/env python3
import os
import sys
import argparse

# JOBS
from jobs.makehelper import makehelper
from jobs.makeinterface import makeinterface
from jobs.makepart import makepart
from jobs.makeplugin import makeplugin
from jobs.makepacket import makepacket
from jobs.maketrait import maketrait

parser = argparse.ArgumentParser()
parser.add_argument("--make-helper", default=None)
parser.add_argument("--make-interface", default=None)
parser.add_argument("--make-part", default=None)
parser.add_argument("--make-plugin", default=None)
parser.add_argument("--make-packet", default=None)
parser.add_argument("--make-trait", default=None)

if __name__ == "__main__":
	args = parser.parse_args()

	if args.make_helper:
		makehelper.do_job(args.make_helper)

	elif args.make_interface:
		makeinterface.do_job(args.make_interface)

	elif args.make_part:
		makepart.do_job(args.make_part)

	elif args.make_plugin:
		makeplugin.do_job(args.make_plugin)

	elif args.make_packet:
		makepacket.do_job(args.make_packet)

	elif args.make_trait:
		maketrait.do_job(args.make_trait)

	else:
		parser.print_help()