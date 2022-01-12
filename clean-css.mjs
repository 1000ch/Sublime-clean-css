import {Buffer} from 'node:buffer';
import getStdin from 'get-stdin';
import CleanCSS from 'clean-css';

getStdin()
  .then(data => minify(data))
  .then(data => process.stdout.write(data));

async function minify(data) {
  const {
    compatibility,
    level,
    format,
    inline
  } = JSON.parse(process.argv[2]);
  const css = Buffer.isBuffer(data) ? data.toString() : data;
  const cleanCSS = new CleanCSS({
    compatibility,
    level,
    format,
    inline,
    returnPromise: true,
  });

  const output = await cleanCSS.minify(css);

  return output.styles;
}
