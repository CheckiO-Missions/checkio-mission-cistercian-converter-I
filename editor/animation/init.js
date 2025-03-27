requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function cistercian_converter_i_visualization(tgt_node, data) {
            if (!data || !data.ext) {
                return
            }
            /**
             * attr
             */
            const attr = {
                scribe: {
                    'stroke-width': '3px',
                    'stroke': '#294270',
                    'stroke-linecap': 'round',
                    'stroke-linejoin': 'round',
                },
            }
            /**
             * value
             */
            const number = data.in
            const draw_area_width_px = 100
            const draw_area_height_px = 110
            /**
             * paper
             */
            const paper = Raphael(tgt_node, draw_area_width_px, draw_area_height_px)
            /**
             * draw cistercian
             */
            const cis = [
                [],
                [['m', 0, -45], ['l', 30, 0]],
                [['m', 0, -15], ['l', 30, 0]],
                [['m', 0, -45], ['l', 30, 30]],
                [['m', 0, -15], ['l', 30, -30]],
                [['m', 0, -15], ['l', 30, -30], ['l', -30, 0]],
                [['m', 30, -15], ['l', 0, -30]],
                [['m', 0, -45], ['l', 30, 0], ['l', 0, 30]],
                [['m', 0, -15], ['l', 30, 0], ['l', 0, -30]],
                [['m', 0, -15], ['l', 30, 0], ['l', 0, -30], ['l', -30, 0]],
            ]
            const conv_quadrant = [
                p => p,
                ([p1, p2, p3]) => [p1, p2 * -1, p3],
                ([p1, p2, p3]) => [p1, p2, p3 * -1],
                ([p1, p2, p3]) => [p1, p2 * -1, p3 * -1],
            ]
            // draw center line
            paper.path(['M', 50, 10, 'v', 90, 'z',]).attr(attr.scribe)
            // draw quadrants
            for (let i = 0; i < 4; i += 1) {
                const tgt_number = Math.trunc(number / 10 ** i) % 10
                paper.path(['M', 50, 55,].concat(cis[tgt_number].map(conv_quadrant[i]))).attr(attr.scribe)
            }
        }
        var io = new extIO({
            animation: function ($expl, data) {
                cistercian_converter_i_visualization(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
