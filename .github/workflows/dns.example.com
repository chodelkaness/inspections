dns.example.com

reverse_proxy 10.0.0.3:80

tls you@example.com {
  # I use cloudflare here for DNS, but you can use any provider
  dns cloudflare {env.CLOUDFLARE_API_TOKEN}
  resolvers 10.0.0.3
}

# Not necessary, but built-in compression can speed things up a bit
encode zstd gzip