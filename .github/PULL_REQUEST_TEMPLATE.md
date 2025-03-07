# Description
_Add a brief description of what this Pull Request encompasses._

## Changes Made
_List bullet points of what changes were done. Record information in the `CHANGELOG.md` with these points if being used with a reference to the Pull Request # and branch name. Changes can be recorded and seen on GitHub if releases/tags are being used instead for the repository._

### Related Issues
_List any issues this Pull Request relates too in order to tie issues with Pull Requests. Refer to the [GitHub Docs](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) for different ways to do this if you want to use closing syntax (auto-close issues after a PR is merged)._

## Preformed Checks / Tests
_List any checks or tests done to the branch if applicable. Put `Not applicable` under this section if it doesn't apply._

_Ex.) Tested CI workflow on private fork_

---------------------

# Pull Request Checklist
_When performing a pull or merge request (PR or MR), ensuring the following are completed helps minimize unnecessary notifications to reviewers and helps ensure your PR is reviewed promptly._

## Before Approval
- [ ] Keep Pull Request in draft state **until** it's ready to be reviewed.
- [ ] Verify Pull Request is Named Correctly.
    - Pull Request **must** have the branch title in the description that is to be merged in.
    - Ex.) `Merge pingraham/initial-dev-guide into develop`
- [ ] Verify/Add assignees to the Pull request.
- [ ] Verify/Add reviewers to the Pull request.
- [ ] Switch Pull Request out of draft state when ready to be reviewed.
  - If you think the reviewer may not already be aware, it is sometimes helpful to notify them the PR is ready by `@`-ing them within the PR to inform them.

## After Approval 
- [ ] Verify all open / unresolved conversations are closed out (if applicable).
  - Conversations _should_ be resolved by the reviewer that made the comment **not** the assignee.
  - If a suggestion is applied within a PR, GitHub will auto-resolves the conversation (this is acceptable).
- [ ] Verify commits are squashed accordingly and or rebase branch for ensuring linear history. 
    - Select the `Squash and Merge` *or equivalent* after approval. *(if applicable)*
    - Refer to the [git-flow-guide](../../computing/git-flow-guide.md) for more information on the different PR options.
- [ ] Verify source / feature branch that was requested to be merged into one of the protected branches is deleted **after** it's merged in successfully.
- [ ] Verify issues tied to Pull Request are closed out accordingly / updated.