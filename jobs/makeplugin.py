from jobs.job import job
import os
from string import Template

class makeplugin(job):

	@staticmethod
	def do_job(plugin_name):

		try:
			os.makedirs('./plugins/{name}/src'.format(name=plugin_name))
		except:
			pass

		yaml = Template('''\
---
name: $name
version: 1.0.0
main: $name\\Main
...
''')
		yaml = yaml.substitute({ 'name': plugin_name })

		code = Template('''\
<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace $name;

use Quizmatix\\plugin\\{PluginBase, PluginEventListener};

class Main extends PluginBase implements PluginEventListener {

	public function onRoomStartTick(Room $room): void
	{
		// room started
	}

}
''')
		code = code.substitute({ 'name': plugin_name, 'room': '$room' })

		file = open('./plugins/{name}/config.yaml'.format(name=plugin_name), "w")
		file.write(yaml)
		file.close()

		file = open('./plugins/{name}/src/Main.php'.format(name=plugin_name), "w")
		file.write(code)
		file.close()

		return True