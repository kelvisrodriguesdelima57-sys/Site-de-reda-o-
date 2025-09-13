// api/gerar_redacao.js
export default async function handler(req, res) {
  if (req.method !== 'POST') {
      return res.status(405).json({ erro: "Método não permitido" });
        }

          const { tema, pontos, tom } = req.body;

            if (!tema || !pontos || !tom) {
                return res.status(400).json({ erro: "Faltam dados obrigatórios" });
                  }

                    try {
                        // ✅ Adicione sua chave e URL da API aqui
                            const SUA_CHAVE_API = "COLOQUE_SUA_CHAVE_AQUI";
                                const URL_SUA_API = "COLOQUE_A_URL_DA_SUA_API_AQUI";

                                    const response = await fetch(URL_SUA_API, {
                                          method: 'POST',
                                                headers: {
                                                        'Content-Type': 'application/json',
                                                                'Authorization': `Bearer ${SUA_CHAVE_API}`
                                                                      },
                                                                            body: JSON.stringify({ tema, pontos, tom })
                                                                                });

                                                                                    const data = await response.json();
                                                                                        res.status(200).json({ texto: data.texto });
                                                                                          } catch (err) {
                                                                                              res.status(500).json({ erro: err.message });
                                                                                                }
                                                                                                }