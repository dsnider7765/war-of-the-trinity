package com.wott.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.wott.game.character.Player;
import com.wott.game.gui.screen.MainScreen;

public class WOTT extends Game {
	SpriteBatch batch;
	Texture img;

	private Player mPlayer;

	@Override
	public void create () {
		setPlayer(new Player());

		Gdx.graphics.setTitle("War of the Trinity");
		setScreen(new MainScreen(this));
		Gdx.input.setInputProcessor((InputProcessor) getScreen());
	}

	public Player getPlayer() {
		return mPlayer;
	}

	public void setPlayer(Player player) {
		mPlayer = player;
	}

	@Override
	public void render () {
        getScreen().render(Gdx.graphics.getDeltaTime());
	}
	
	@Override
	public void dispose () {
		getScreen().dispose();
	}


}
