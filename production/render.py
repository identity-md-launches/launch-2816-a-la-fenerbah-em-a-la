#!/usr/bin/env python3
"""Offline encoder. Requires Python 3, ffmpeg, ffprobe; cards are delivered assets."""
import concurrent.futures,json,pathlib,subprocess,tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1]
def run(args):subprocess.run(args,cwd=ROOT,check=True,stdout=subprocess.DEVNULL)
def main():
 with tempfile.TemporaryDirectory(prefix='fenerbahce-') as work:
  tmp=pathlib.Path(work)
  def shot(i):
   # Modest optical push preserves typography and original jersey marks.
   z='1+0.014*on/119' if i%2==0 else '1.014-0.014*on/119'
   vf=f"zoompan=z='{z}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=120:s=1920x1080:fps=24,setsar=1"
   if i==0:vf+=',fade=t=in:st=0:d=1'
   elif i%3==0:vf+=',fade=t=in:st=0:d=0.18'
   if i==35:vf+=',fade=t=out:st=3:d=2'
   elif i%3==2:vf+=',fade=t=out:st=4.82:d=0.18'
   out=tmp/f'{i:02d}.mp4'
   run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',f'production/cards/{i:02d}.jpg','-vf',vf,'-frames:v','120','-an','-c:v','libx264','-preset','medium','-crf','21','-maxrate','2200k','-bufsize','4400k','-pix_fmt','yuv420p','-threads','2','-video_track_timescale','12288',str(out)])
   print(f'Encoded shot {i+1}/36',flush=True)
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(shot,range(36)))
  (tmp/'concat.txt').write_text(''.join(f"file '{tmp}/{i:02d}.mp4'\n" for i in range(36)))
  data=json.loads((ROOT/'production/storyboard.json').read_text())
  metadata=';FFMETADATA1\ntitle=AĞLA FENERBAHÇEM AĞLA\ncomment=Silent reference-based photographic animatic; see README for limitations.\n'
  for i in range(12):metadata+=f'[CHAPTER]\nTIMEBASE=1/1000\nSTART={i*15000}\nEND={(i+1)*15000}\ntitle={data[i*3]["chapter"]}\n'
  (tmp/'chapters.txt').write_text(metadata)
  (ROOT/'artifacts').mkdir(exist_ok=True)
  run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(tmp/'concat.txt'),'-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-f','ffmetadata','-i',str(tmp/'chapters.txt'),'-map','0:v:0','-map','1:a:0','-map_metadata','2','-map_chapters','2','-c:v','copy','-c:a','aac','-b:a','128k','-t','180','-movflags','+faststart','artifacts/video.mp4'])
if __name__=='__main__':main()
