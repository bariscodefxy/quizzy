from jobs.job import job
from string import Template

class makehelper(job):

	@staticmethod
	def do_job(helper_name):

		base_code = Template('''\
<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\\helpers;

use Quizmatix\\interface\\HelpersInterface;

class $classname implements HelpersInterface
{
	
	/**
	  * Example function
	  */
	public function foo(): array
	{
		return ['Successfully', 'created', 'the', 'helper', '.'];
	}

} 
''')
		base_code = base_code.substitute({ 'classname': helper_name })
		
		file = open("./src/helpers/" + helper_name + ".php", "w");
		file.write(base_code)
		file.close()

		return True