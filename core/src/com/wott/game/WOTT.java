package com.wott.game;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Game;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.wott.game.gui.screen.MainScreen;

public class WOTT extends Game {
	SpriteBatch batch;
	Texture img;
	
	@Override
	public void create () {
		Gdx.graphics.setTitle("War of the Trinity");
		setScreen(new MainScreen(this));
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
