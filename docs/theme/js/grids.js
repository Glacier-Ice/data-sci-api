/*
 * this is a modified recreation of @jackrugile's awesomepen:
 * Rainbow Grid https://codepen.io/jackrugile/details/bdwvMo/
 *
 * I have no credit over the idea, but the code is original and side option comes from this pen
 */
document.addEventListener('DOMContentLoaded', function () {
    let c = document.getElementById('grids');

    var w = c.width = window.innerWidth,
        h = c.height = window.innerHeight,
        ctx = c.getContext('2d'),

        opts = {
            lineMaxCount: 70,
            lineSpawnProb: .2,
            lineMaxLength: 10,
            lineIncrementProb: .4,
            lineDecrementProb: .7,
            lineSafeTime: 150,
            lineMidJitter: 7,
            lineMidPoints: 3,
            lineHueVariation: 50,
            lineAlpha: 1,

            gridSideNum: 9,
            gridSide: 70,
            gridRotationVel: .002,
            gridScalingInputMultiplier: .01,
            gridScalingMultiplier: .3,
            gridHueChange: .4,
            gridRepaintAlpha: .1,
            gridCenterX: w / 2,
            gridCenterY: h / 2
        },

        tick = (Math.random() * 360),
        lines = [],
        linePart, s,
        radPart = Math.PI * 2 / opts.gridSideNum;

    function loop() {

        window.requestAnimationFrame(loop);

        loop.step();
        loop.draw();
    }

    loop.step = function () {

        loop.step.spawn();
        loop.step.updateTick();

        lines.map(function (line) { line.step(); });
    }
    loop.draw = function () {

        linePart = 1 / opts.lineMidPoints;
        s = opts.gridSide;

        loop.draw.repaint();
        loop.draw.transform();

        lines.map(function (line) { line.draw(); });

        ctx.restore();
    }

    loop.step.spawn = function () {

        if (lines.length < opts.lineMaxCount && Math.random() < opts.lineSpawnProb)
            lines.push(new Line);
    }
    loop.step.updateTick = function () {

        ++tick;
    }
    loop.draw.repaint = function () {

        ctx.globalCompositeOperation = 'destination-out';
        ctx.fillStyle = 'rgba(0,0,0,alp)'.replace('alp', opts.gridRepaintAlpha);
        ctx.fillRect(0, 0, w, h);
        ctx.globalCompositeOperation = 'lighter';
    }
    loop.draw.transform = function () {

        ctx.save();
        var scaleFactor = 1 + Math.sin(tick * opts.gridScalingInputMultiplier) * opts.gridScalingMultiplier;

        ctx.translate(opts.gridCenterX, opts.gridCenterY);
        ctx.rotate(tick * opts.gridRotationVel);
        ctx.scale(scaleFactor, scaleFactor);

        ctx.lineWidth = .2;
    }

    function Line() {

        this.reset();
    }
    Line.prototype.reset = function () {

        this.head = new Vec(0, 0);
        this.path = [this.head];

        this.life = 0;
        this.hue = ((tick * opts.gridHueChange) % 360) | 0;
    }

    Line.prototype.step = function () {

        ++this.life;

        this.step_increment();
        this.step_decrement();
    }
    Line.prototype.draw = function () {

        if (this.path.length === 0) return;

        var x1 = this.path[0].x,
            y1 = this.path[0].y,
            x2, y2, dx, dy;

        for (var i = 1; i < this.path.length; ++i) {
            // I start from 1 intentionally, so that I don't have to do any checkings

            ctx.strokeStyle = 'hsla(hue, 80%, 50%, alp)'
                .replace('hue', this.hue + (Math.random() * opts.lineHueVariation) | 0)
                .replace('alp', opts.lineAlpha / (this.life / 80));

            x2 = this.path[i].x;
            y2 = this.path[i].y;

            dx = (x2 - x1) / opts.lineMidPoints;
            dy = (y2 - y1) / opts.lineMidPoints;

            ctx.beginPath();
            ctx.moveTo(x1 * s + Math.random() * opts.lineMidJitter - opts.lineMidJitter / 2, y1 * s + Math.random() * opts.lineMidJitter - opts.lineMidJitter / 2);

            for (var j = 1; j < opts.lineMidPoints - 1; ++j)
                ctx.lineTo(
                    // initial + step portion + jitter
                    (x1 + dx * j) * s + Math.random() * opts.lineMidJitter - opts.lineMidJitter / 2,
                    (y1 + dy * j) * s + Math.random() * opts.lineMidJitter - opts.lineMidJitter / 2
                );

            ctx.lineTo(x2 * s + Math.random() * opts.lineMidJitter - opts.lineMidJitter / 2, y2 * s + Math.random() * opts.lineMidJitter - opts.lineMidJitter / 2);
            ctx.stroke();

            x1 = x2;
            y1 = y2;
        }
    }
    Line.prototype.step_increment = function () {

        if (Math.random() > opts.lineIncrementProb) return;

        var vec,
            lastHead = this.path[this.path.length - 2];

        do {

            vec = randomPos(this.head);
        } while (lastHead && vec.x === lastHead.x && vec.y === lastHead.y);

        this.head = vec;
        this.path.push(vec);

        if (this.path.length >= opts.lineMaxLength) this.path.shift();
    }
    Line.prototype.step_decrement = function () {

        if (this.life < opts.lineSafeTime || Math.random() > opts.lineDecrementProb) return;

        this.path.length > 0 ?
            this.path.shift()
            :
            this.reset();

    }

    function Vec(x, y) {

        this.x = x;
        this.y = y;
    }

    function randomPos(previous) {

        var rad = radPart * ((Math.random() * opts.gridSideNum) | 0);

        return new Vec(Math.cos(rad) + previous.x, Math.sin(rad) + previous.y);
    }

    loop();

});