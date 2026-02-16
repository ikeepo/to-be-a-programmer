# Emmet
[docs](https://emmet.io/), [emmet-vim](https://mattn.github.io/emmet-vim/)
[Tutorial](https://raw.githubusercontent.com/mattn/emmet-vim/master/TUTORIAL)
## lazy.vim
```shell 
:Mason
Find the emmet-language-server 
i for install 
# go to nvim-lspconfig 

    config = function(_, opts)
      local lspconfig = require("lspconfig")
      for server, config in pairs(opts.servers) do
        -- passing config.capabilities to blink.cmp merges with the capabilities in your
        -- `opts[server].capabilities, if you've defined it
        config.capabilities = require("blink.cmp").get_lsp_capabilities(config.capabilities)
        lspconfig[server].setup(config)
      end
      -- emmet
      lspconfig.emmet_language_server.setup({
        filetypes = { "html", "css", "javascriptreact", "typescriptreact", "vue", "next" },
      })
    end,
```

## Refs 
- [r1](https://www.youtube.com/watch?v=QYnPVXZ_BH0)
