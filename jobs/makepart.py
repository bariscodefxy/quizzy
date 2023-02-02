from jobs.job import job
from string import Template

class makepart(job):

	@staticmethod
	def do_job(part_name):

		base_code = Template('''\
<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\\parts;

class $classname
{

    public function __get($variable)
    {
        return $this->{$variable};
    }
    
    public function __set($variable, $value)
    {
        $this->{$variable} = $value;
    }

} 
''')
		base_code = base_code.substitute({ 'classname': part_name, 'variable': '$variable', 'value': '$value', 'this': '$this' })
		
		file = open("./src/parts/" + part_name + ".php", "w");
		file.write(base_code)
		file.close()

		return True