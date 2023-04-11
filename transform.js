function query(data) {
  return {
    id: data.id,
    uri: data.uri,
    url: data.external_urls.spotify,
    ownerName: data.owner.display_name,
    ownerId: data.owner.id,
    tracks: data.tracks.items.map((item) => {
      return {
        id: item.track.id,
        uri: item.track.uri,
        url: item.track.external_urls.spotify,
        name: item.track.name,
      };
    }),
  };
}
