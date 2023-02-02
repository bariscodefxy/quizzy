<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\protocol;

use Quizmatix\MainServer;
use Quizmatix\player\Player;

class TestPacket extends PacketBase implements Packet {

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
