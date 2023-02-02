from jobs.job import job
from string import Template

class maketrait(job):

	@staticmethod
	def do_job(trait):

		base_code = Template('''\
<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\\traits;

trait $name
{
	private string $foo = "";

	public function __construct(string $foo = "") {
		$this->foo = $foo;
	}

	public function getFoo(): string {
		return $this->foo;
	}

	public function setFoo(string $foo): void {
		$this->foo = $foo;
	}

	public function __toString(): string {
		return $this->foo;
	}
}
''')
		base_code = base_code.substitute({ 'name': trait, 'foo': '$foo', 'this': '$this' })

		file = open("./src/traits/{name}Trait.php".format(name=trait), "w")
		file.write(base_code)
		file.close()

		return True