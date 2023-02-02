<?php

/**
  * This code auto generated with Quizzy CLI
  *
  * 2023 (c) Quizzy CLI by bariscodefx
  *
  */

namespace TestPlugin;

use Quizmatix\plugin\{PluginBase, PluginEventListener};

class Main extends PluginBase implements PluginEventListener {

	public function onRoomStartTick(Room $room): void
	{
		// room started
	}

}
