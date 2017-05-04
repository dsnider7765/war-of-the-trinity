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
        Texture texture = new Texture(Gdx.files.internal("sprites/DEBUG-encounter.png"));
        TextureRegion textureRegion = new TextureRegion(texture, 100, 100);
        mSprite = new Sprite(textureRegion);
    }

    public Sprite getSprite() {
        return mSprite;
    }

    public void setSprite(Sprite sprite) {
        mSprite = sprite;
    }
}
