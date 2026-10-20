<template>
  <figure class="vp-video">
    <video
      class="vp-video-player"
      :src="src"
      :poster="poster"
      controls
      preload="none"
      playsinline
      :width="width || '100%'"
    >
      你的浏览器不支持视频播放，请升级浏览器或换用 Chrome / Edge。
    </video>
    <figcaption v-if="caption" class="vp-video-caption">{{ caption }}</figcaption>
  </figure>
</template>

<script setup>
defineProps({
  // 视频地址，放在 docs/public/videos/ 下时写 /videos/xxx.mp4
  src: { type: String, required: true },
  // 封面图，可用手册截图，避免加载首帧流量
  poster: { type: String, default: '' },
  // 视频下方说明文字
  caption: { type: String, default: '' },
  width: { type: [String, Number], default: '100%' }
})
</script>

<style scoped>
.vp-video {
  margin: 1.5rem 0;
}
.vp-video-player {
  display: block;
  width: 100%;
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
  background: #000;
}
.vp-video-caption {
  margin-top: 0.5rem;
  text-align: center;
  font-size: 14px;
  color: var(--vp-c-text-2);
}
</style>
