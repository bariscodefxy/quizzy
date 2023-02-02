from jobs.job import job
from string import Template

class makepacket(job):

	@staticmethod
	def do_job(packet_name):

		base_code = Template('''\
<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\\protocol;

use Quizmatix\\MainServer;
use Quizmatix\\player\\Player;

class $name extends PacketBase implements Packet {

    private int $foo;

    public function __construct($args) {
        parent::__construct($args);
        $this->foo = $args['bar'];
    }

    public function getFoo(): ?int
    {
    	return $this->foo;
    }

    public function setFoo(int $foo): void {
        $this->foo = $foo;
    }

}
''')
		base_code = base_code.substitute({ 'name': packet_name + 'Packet', 'foo': '$foo', 'args': '$args', 'this': '$this' })

		file = open("./src/protocol/{name}Packet.php".format(name=packet_name), "w")
		file.write(base_code)
		file.close()

		return True