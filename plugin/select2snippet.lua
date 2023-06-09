-- Last Modified: 2023-06-08 19:26:23

-- 检查当前 NeoVim 是否支持 Python 3
if vim.fn.has('python3') ~= 1 then
  print("[ERROR] NeoVim does not support Python 3!")
  return
end

-- 加载 Python 支持插件
local ok, pynvim = pcall(require, 'pynvim')
if not ok then
  print("[ERROR] Failed to load pynvim module: " .. pynvim)
  return
end

local M = {}

vim.cmd('nnoremap <leader>cw :Select2Snippet word<CR>')
vim.cmd('nnoremap <leader>cl :Select2Snippet line<CR>')
im.cmd('vnoremap <leader>cs :Select2Snippet select<CR>')
