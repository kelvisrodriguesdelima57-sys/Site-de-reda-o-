const speedInsights = require('@vercel/speed-insights');

async function testarSite(url) {
    const result = await speedInsights.run(url);
        console.log(result);
        }

        // Troque a URL pelo site que você quer testar
        testarSite('https://gerador-de-reda-os-b34f.vercel.app/