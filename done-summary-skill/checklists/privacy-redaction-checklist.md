# Privacy Redaction Checklist

Use this checklist before publishing or sharing a Done Summary outside the original project.

- [ ] Remove API keys, tokens, private keys, passwords, cookies, session IDs, and auth headers.
- [ ] Remove private phone numbers, emails, addresses, customer names, and account IDs.
- [ ] Remove private local filesystem paths unless they are safe and intentionally public.
- [ ] Replace internal URLs, deployment IDs, database names, and project names when they expose sensitive context.
- [ ] Replace real client, employee, or partner names with neutral labels.
- [ ] Remove private business strategy, pricing, legal, financial, or operational details.
- [ ] Keep only the pattern of the lesson when the real example is sensitive.
- [ ] Mark unverified claims as unverified instead of making them sound final.
- [ ] Re-read the summary as a public reader and check whether any hidden context can identify a private project.
- [ ] Prefer a sanitized example for public repositories.
