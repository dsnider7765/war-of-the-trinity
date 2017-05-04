package com.wott.game.game.encounter;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.TextureRegion;

/**
 * Created by student on 5/4/17.
 */
public class Encounter {
    private Sprite mSprite;

    public Encounter(){
        mSprite = new Sprite(new Texture(Gdx.files.internal("sprites/Generic Test Encounter.png")));
    }

    public Sprite getSprite() {
        return mSprite;
    }

    public void setSprite(Sprite sprite) {
        mSprite = sprite;
    }
}
