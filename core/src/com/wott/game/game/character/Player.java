package com.wott.game.game.character;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;

/**
 * Created by student on 5/3/17.
 */
public class Player {
    private Sprite mSprite;

    public Player() {
        mSprite = new Sprite(new Texture(Gdx.files.internal("sprites/CaptainGeneric.png")));
    }

    public Sprite getSprite() {
        return mSprite;
    }

    public void setSprite(Sprite sprite) {
        mSprite = sprite;
    }
}
