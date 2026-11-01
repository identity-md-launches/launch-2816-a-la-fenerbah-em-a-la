#!/usr/bin/env python3
"""Validate delivered media and write a machine-readable QC record."""
import json,pathlib,subprocess,hashlib,struct
root=pathlib.Path(__file__).resolve().parents[1]
p=root/'artifacts/video.mp4'
def capture(args):return subprocess.check_output(args,cwd=root,text=True)
probe=json.loads(capture(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-show_chapters','-of','json','artifacts/video.mp4']))
v=next(s for s in probe['streams'] if s['codec_type']=='video')
a=next(s for s in probe['streams'] if s['codec_type']=='audio')
assert v['codec_name']=='h264' and v['pix_fmt']=='yuv420p'
assert (v['width'],v['height'])==(1920,1080)
assert int(v['nb_read_frames'])==4320 and v['r_frame_rate']=='24/1'
assert a['codec_name']=='aac' and a['channels']==2 and a['sample_rate']=='48000'
assert abs(float(probe['format']['duration'])-180)<.05
assert p.stat().st_size<64*1024**2
assert len(probe['chapters'])==12
subprocess.run(['ffmpeg','-v','error','-xerror','-i','artifacts/video.mp4','-f','null','-'],cwd=root,check=True)
atoms=[]
with p.open('rb') as fp:
 while True:
  offset=fp.tell();header=fp.read(8)
  if len(header)<8:break
  size,kind=struct.unpack('>I4s',header)
  if size==1:size=struct.unpack('>Q',fp.read(8))[0]
  atoms.append({'type':kind.decode('ascii'),'offset':offset,'size':size})
  if not size:break
  fp.seek(offset+size)
assert next(x['offset'] for x in atoms if x['type']=='moov')<next(x['offset'] for x in atoms if x['type']=='mdat')
result={'output':'artifacts/video.mp4','duration_seconds':float(probe['format']['duration']),'width':v['width'],'height':v['height'],'fps':24,'decoded_video_frames':int(v['nb_read_frames']),'video_codec':v['codec_name'],'pixel_format':v['pix_fmt'],'audio_codec':a['codec_name'],'audio_sample_rate':48000,'audio_channels':2,'audio_content':'Digital silence; no supplied song','bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'chapters':len(probe['chapters']),'fast_start':True,'full_decode':'passed; ffmpeg -xerror produced no errors','mp4_atoms':atoms,'visual_qc':'All three accessible reference images inspected; sample composited cards and encoded frame contact sheet inspected. Original jersey marks and PNG crest retained. See README for substantial missing performance/action scenes.','limitations':['Reference-based photographic animatic, not a generated live-action music video','No generative-video capability available','Interior reference DNS failure; merchandise page HTTP 403','No Suno audio supplied','Real exterior image upscaled from 780x470','No crying or moving supporters, players, flags, goals, management/transfer performances or seated-fan ending']}
(root/'production/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
