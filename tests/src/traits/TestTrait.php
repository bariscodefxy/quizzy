<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace Quizmatix\traits;

trait Test
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
