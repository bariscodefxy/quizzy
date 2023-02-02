from jobs.job import job
from string import Template

class makeinterface(job):

	@staticmethod
	def do_job(interface_name):

		base_code = Template('''\
<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\\interfaces;


interface $iname
{
	
	// Example
	public function foo(): array;

} 
''')
		base_code = base_code.substitute({ 'iname': interface_name + "Interface" })
		
		file = open("./src/interfaces/" + interface_name + "Interface.php", "w");
		file.write(base_code)
		file.close()

		return True